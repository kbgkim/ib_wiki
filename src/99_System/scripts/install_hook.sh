#!/bin/bash

# 프로젝트 최상위 디렉토리로 이동 (스크립트 위치 무관하게 작동)
REPO_ROOT=$(git rev-parse --show-toplevel)
HOOK_PATH="$REPO_ROOT/.git/hooks/pre-commit"
SCRIPT_PATH="src/99_System/scripts/update_readme_date.py"

echo "Installing Git pre-commit hook..."

# pre-commit 파일이 없으면 생성, 있으면 내용 추가
if [ ! -f "$HOOK_PATH" ]; then
    echo "#!/bin/bash" > "$HOOK_PATH"
fi

# 이미 스크립트 호출 코드가 들어있는지 확인
if grep -q "$SCRIPT_PATH" "$HOOK_PATH"; then
    echo "Hook is already installed."
else
    echo "" >> "$HOOK_PATH"
    echo "# Auto-update README date" >> "$HOOK_PATH"
    echo "python3 $SCRIPT_PATH" >> "$HOOK_PATH"
    echo "git add README.md" >> "$HOOK_PATH"
    echo "Done. Hook added to $HOOK_PATH"
fi

# 실행 권한 부여
chmod +x "$HOOK_PATH"

echo "Installation complete."
