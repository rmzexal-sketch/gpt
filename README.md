# Ai PDF v0.0008 · 최신 UI-r4 작업본

[최신 실행용 ZIP 다운로드 — 약 30MB](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/ui-r4/AiPDF-v0.0008-ui-r4-runtime.zip)

압축을 풀고 `AiPDF-v0.0008.exe`를 실행합니다. Windows x64, SSE4.1 CPU 대상이며 사용자 Python·Visual Studio 설치가 필요하지 않습니다.

공통 화면은 Direct2D/DirectWrite/WIC 기반입니다. PDF 공유 입력·창 전체 드롭·시계/음력·미저장 편집 보호·PDF 편집 부분 기능·페이지 분리·공통 Excel·검토 후 파일명변경을 포함합니다.

Wine에서 3회 각각 230개 GUI 확인과 실제 저장 PDF의 독립 렌더링 대조를 통과했습니다. 실제 Windows 시험은 미검증이며 전체 프로그램은 미완료입니다. BoltPDF 통합과 실제 AI 모델 추론은 포함되지 않습니다. 600 DPI 타일·전체 편집·6-AI 자동 큐·최종 단일 통합 보고서는 미완료입니다.

[기능별 완료/미해결 현황](downloads/ui-r4/RELEASE-STATUS.md)

## 전체 소스·로그 패키지

GitHub의 단일 파일 제한에 맞춰 전체 ZIP을 80MiB씩 세 부분으로 나눴습니다. 같은 폴더에 아래 파일 네 개를 내려받고 `Restore-AiPDF-full.cmd`를 실행하면 전체 ZIP이 복원됩니다. 실행용 ZIP만 이용할 때에는 이 과정이 필요하지 않습니다.

- [전체 ZIP 001](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/ui-r4/AiPDF-v0.0008-ui-r4-full.zip.001)
- [전체 ZIP 002](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/ui-r4/AiPDF-v0.0008-ui-r4-full.zip.002)
- [전체 ZIP 003](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/ui-r4/AiPDF-v0.0008-ui-r4-full.zip.003)
- [전체 ZIP 복원 명령](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/ui-r4/Restore-AiPDF-full.cmd)
- [크기·SHA256](downloads/ui-r4/SHA256.json)

전체 패키지 안의 `source/`에 애플리케이션·MuPDF·cJSON·음력 데이터의 대응 소스와 라이선스가 들어 있습니다. GNU AGPL v3 및 포함된 제3자 라이선스가 적용됩니다.

아래 Word-runtime 배포본은 이전 개발 이력이며 최신 UI가 아닙니다.

---

# Ai PDF v0.0008 Word 통합 개발 배포본

[실행용 ZIP 다운로드](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/AiPDF-v0.0008-Word-runtime.zip)

[Windows x64 EXE 다운로드](https://github.com/rmzexal-sketch/gpt/raw/refs/heads/aipdf-download-0008/downloads/AiPDF-v0.0008-Word-Windows-x64.exe)

ZIP 압축을 풀고 `AiPDF-v0.0008.exe`를 실행합니다. 별도 Python·Word·PDF 엔진 DLL 설치 없이 동작하도록 빌드했습니다. Windows 10/11 x64, SSE4.1 CPU 대상입니다.

- PDF·Excel은 첫 줄 일련번호만 비교하고, PASS 이후 메뉴 3을 활성화합니다.
- Excel `AiPDF_AI` 시트의 AI 결과 텍스트를 일련번호순 DOCX로 통합합니다.
- AI별 미완성본을 저장하고, 모든 기대 번호의 상태가 완성일 때만 완성본도 저장합니다.
- 사용법과 입력 형식은 [USAGE.md](USAGE.md)를 확인하세요.
- Wine에서 Win32 GUI 3회 각 50개 검증 및 실제 DOCX 재열기를 완료했습니다. 실제 Microsoft Windows 장치 시험은 미완료입니다.
- PDF 편집/분리, 외부 AI 자동 호출, 도면 분석은 미구현입니다.

## 대응 소스

`source/`에 애플리케이션과 링크한 MuPDF·하위 의존성의 전체 대응 소스를 분할 저장했습니다. `source/REASSEMBLE.txt` 명령으로 합칩니다. 이 소스가 실행에 필요한 것은 아닙니다.

GNU AGPL v3 및 포함된 제3자 라이선스가 적용됩니다.
