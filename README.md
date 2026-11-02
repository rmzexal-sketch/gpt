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
