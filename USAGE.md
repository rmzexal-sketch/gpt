# Ai PDF v0.0008 — Windows x64 개발 배포본

`dist/AiPDF-v0.0008-Word-Windows-x64.zip`을 압축 해제하고 `AiPDF-v0.0008.exe`를 실행합니다.
MuPDF 1.26.11을 정적으로 포함합니다. Python, Excel 설치, 별도 PDF DLL, VC++ 재배포 설치가 필요 없습니다. Windows 10/11 x64, SSE4.1 CPU 대상입니다.
전체 Ai PDF 기능이 완성된 제품은 아닙니다. 아래 현재 기능과 제한을 확인하세요.

## AI별 Word 자동 통합 (추가 구현)

검사에 사용한 동일 Excel에 `AiPDF_AI` 시트를 만듭니다. 1행은 `ai`, `serial`, `status`, `text`이고 A~D열 순서입니다. `serial`은 PDF·Excel 일치 검사에서 확인된 실제 일련번호입니다.

- `ai`: AI 이름. 최대 6개를 별도 그룹으로 처리합니다.
- `status`: `complete`/`완성` 또는 `pending`/`미완성`. 완성은 입력 데이터의 상태 선언이며 AI 결과의 정답을 보증하는 표시는 아닙니다.
- `text`: 결과 텍스트. 한글, 줄바꿈, 탭을 Word에 저장합니다. 완성 상태의 빈 본문은 거부합니다.
- 메뉴 2 검사 PASS 후 메뉴 3에서 저장 폴더를 고르면 자동 통합합니다.
- PDF 페이지나 Excel 행 순서와 무관하게 **숫자 일련번호 오름차순**으로 저장합니다.
- AI마다 `AI-01`, `AI-02` 등의 별도 폴더를 만들며 `AI.txt`에 실제 이름을 저장합니다.
- 모든 AI에 `미완성본.docx`를 저장합니다. 해당 AI의 모든 기대 번호가 존재하고 모두 완성이면 `완성본.docx`도 추가 저장합니다. 누락은 `MISSING`, 진행 중은 `PENDING`으로 표시합니다.
- 재실행 시 새 실행 폴더를 만들어 이전 미완성본/완성본을 덮어쓰지 않습니다. `.partial`은 저장이 완료되지 않은 실행이므로 완성 결과로 사용하지 않습니다.
- 중복/알 수 없는 번호·잘못된 상태·수식·빈 완성 결과를 거부합니다. 입력 변경 시 재검사 전까지 저장할 수 없습니다.
- `summary.txt`에 AI별 완성 여부와 입력 PDF/Excel SHA-256을 기록합니다.
- Word 설치나 Python 없이 DOCX를 생성합니다. 기존 DOCX의 이미지·표·서식을 병합하는 기능은 아니며 Excel에 등록된 AI 결과 텍스트를 통합합니다. 외부 AI 자동 호출·도면 분석은 아직 구현하지 않았습니다.

현재 개발·입력·생성·시험·배포 자료는 `/workspace/library-files/PDF` 아래에 보관합니다. ChatGPT 계정 라이브러리 동기화는 확인되지 않았습니다.

## 변경된 일치 검사 기준

사용자 최종 지시에 따라 **PDF 각 페이지의 맨앞줄 일련번호(페이지번호)와 Excel의 `page` 값 하나만 비교**합니다. 본문 전체 일치 조건은 폐기했습니다. 본문·다른 열·다른 열의 수식은 검사하지 않습니다.

- Excel 형식: `.xlsx`, 시트 이름 `AiPDF_Match`, A1=`page`.
- A2부터 PDF 페이지 순서대로 각 페이지의 첫 줄 번호를 입력합니다. `text` 열은 필요 없습니다. 다른 열은 무시합니다.
- 각 페이지에서 시각적으로 가장 위, 같은 높이면 가장 왼쪽의 비어 있지 않은 텍스트 줄을 사용합니다. PDF 내부 객체 저장 순서가 기준은 아닙니다.
- 지원 예: `1`, `001`, `1 제목`, `Page: 1`, `페이지: 1`, `일련번호: 1`. 양의 정수 최대 8자리이며 앞의 0은 무시합니다.
- Excel A열의 해당 번호는 PDF에서 읽은 번호와 같아야 합니다. 번호는 반드시 PDF 실제 텍스트에서 읽습니다. 단순히 PDF의 물리적 페이지 순번을 가정하지 않습니다.
- 모든 페이지의 번호와 행 개수가 맞아야 PASS입니다. 번호 불일치·페이지 누락/추가·A열 수식·잘못된 파일은 통과하지 않습니다.
- 스캔/그림뿐인 페이지, 첫 줄 번호가 없는 페이지, 암호가 필요한 PDF는 BLOCKED입니다. OCR과 영문·한글 숫자 표현(일/이/삼), 임의 영숫자 도면번호는 지원하지 않습니다.
- 빈 여분 행이나 `page`가 아닌 기존 대장 양식은 자동으로 추측하지 않습니다.

예: PDF 첫 페이지 첫 줄 `일련번호: 101`, 두 번째 페이지 첫 줄 `102`라면 Excel A2=101, A3=102. 본문은 서로 달라도 PASS입니다.

## 메뉴와 원본 보존

1. 메뉴 1: 원본 PDF를 다른 경로에 복사합니다. 기존 파일/원본 덮어쓰기는 Windows `CREATE_NEW`로 거부합니다. PDF 편집 기능은 아직 없습니다.
2. 메뉴 2: 실제 PDF와 Excel을 선택해 위 번호 검사를 합니다. PDF 분리 및 대장 자동 생성은 아직 없습니다.
3. 메뉴 3: 검사 PASS 후에만 버튼이 활성화됩니다. 저장 폴더를 선택하면 위 AI별 Word 통합을 실행합니다. 외부 AI 호출과 도면 분석은 아직 없습니다.

새 선택·취소·검사 실패는 이전 PASS를 폐기합니다. PASS 이후 두 파일의 전체 SHA-256을 주기적으로, 메뉴 3 사용 직전에 다시 확인합니다. 파일 변경/삭제/읽기 실패가 감지되면 다시 잠기며 파일을 원복해도 명시적 재검사가 필요합니다. 본문만 바뀐 경우도 변경 시 잠기지만 재검사에서 번호가 맞으면 다시 PASS입니다.
Word 생성은 해시가 일치하는 Excel 메모리 스냅샷을 사용하며, 저장 전/후 파일 상태를 다시 검사하고 새 결과 디렉터리를 커밋합니다. 외부 AI 작업은 아직 없습니다.

## Word 검증

C17 Word 코어의 1차/2차/3차 시험은 각각 7/17/19건을 통과했습니다. 실제 Windows PE CLI는 Wine에서 각각 10/27/47개 검증을 통과했고, Word 폴더 선택·파일 생성·잠금/복구까지 포함한 실제 Win32 GUI는 세 회차 모두 50개 검증을 통과했습니다. 실제 Microsoft Windows 장치 시험은 미수행입니다.
`evidence/word-stage*.log`, `evidence/windows-word-stage*.log`, `evidence/windows-word-gui-stage*.log`에 증거가 있으며 입력과 DOCX는 해당 시험 폴더에 남겨두었습니다.

## 검증 구분

- Linux C17·MuPDF 번호 검사: 1차 16건, 2차 13건, 3차 27건. `evidence/serial-stage*.log` 및 실제 PDF/XLSX, SHA-256 JSON.
- 실제 Windows PE 실행 파일: Wine 10.0에서 실행합니다. Windows 파일 열기·선택, 실제 버튼 활성화, 번호 불일치, 외부 파일 변경 재잠금, 복구, 취소, 정상 종료를 세 단계로 확인합니다. `evidence/windows-gui-serial-stage*.log`.
- Windows CLI 실행 파일: 실제 PDF/XLSX 10종과 Windows 안전 복사 시험을 세 단계로 실행합니다. `evidence/windows-cli-stage*.log`.
- 압축 배포본을 다시 풀어서 동일 GUI 시험과 PE/DLL 의존성·해시 무결성을 확인합니다. `evidence/windows-package.log`.
- 실제 Microsoft Windows 장치에서 실행한 결과는 **UNVERIFIED**입니다. Wine 실행 결과와 구분합니다.
- `evidence/match-*`는 이전 본문 전체 검사 기준의 과거 기록입니다. 현재 번호 전용 기준의 통과 증거로 사용하지 않습니다.
- 초기 Wine 설정/GUI 시험 자동화 실패 기록도 남겨두었습니다. 최종 로그의 완료와 종료 상태로 판정합니다.

## 재현 빌드

애플리케이션은 C17 + Win32입니다. `tools/build-windows-cross.sh`는 MuPDF 소스와 MinGW GCC/G++ 14 도구를 사용해 정적 링크합니다. `MUPDF_SOURCE`, `MINGW_BIN`으로 경로를 지정할 수 있습니다.
MuPDF 출처, 태그, 정확한 하위 의존성 커밋은 `evidence/dependencies.json`에 있습니다. `tools/verify-match.sh`는 Linux 시험, `tests/test_windows_run.py`와 `tests/test_windows_gui.c`는 Windows PE 시험입니다. Python은 테스트 도구일 뿐 최종 EXE 런타임 의존성이 아닙니다.

## 라이선스와 소스

이 결합 배포물은 GNU AGPL v3 조건으로 제공합니다. MuPDF 및 포함된 제3자 구성요소 고지는 소스와 `LICENSE`/`THIRD-PARTY.txt`에 있습니다. GCC 런타임에는 GCC Runtime Library Exception이 적용됩니다.
배포 ZIP의 `source/AiPDF-v0.0008-source.tar.gz`에 애플리케이션 전체 소스, 빌드/시험 스크립트, 실제 시험 자료 및 링크한 MuPDF와 하위 의존성의 대응 소스를 포함합니다.

## 미해결과 최종 Windows 시험

확정 Word 개발 기준서/GUI/폴더/경고음 정책은 제공되지 않았습니다. BoltPDF, PDF 편집/분리, 외부 AI 호출, 도면분석은 완성하지 않았습니다. AI 결과 텍스트의 Word 통합은 위 범위에서 구현했습니다. 이 배포본이 전체 기능 PASS라는 뜻은 아닙니다.
최종 Windows 시험 항목 하나: 번호가 같은 PDF·Excel 선택 → 메뉴 3 활성화 → 파일 수정 → 재잠금 → 다른 번호 검사 시 잠금 유지 → 본문이 달라도 번호가 같은 자료로 재검사 후 활성화.
