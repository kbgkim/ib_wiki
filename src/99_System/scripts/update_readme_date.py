import re
import datetime
import os

def update_readme_date():
    readme_path = 'README.md'
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found.")
        return

    # 오늘 날짜 (YYYY-MM-DD)
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # '최종 업데이트: YYYY-MM-DD' 패턴 찾기
    pattern = r'(- \*\*최종 업데이트\*\*: )(\d{4}-\d{2}-\d{2})'
    
    if not re.search(pattern, content):
        print("Warning: '최종 업데이트' pattern not found in README.md")
        return

    new_content = re.sub(pattern, rf'\g<1>{today}', content)

    if content == new_content:
        print(f"README.md is already up to date ({today}).")
    else:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated README.md date to {today}.")

if __name__ == "__main__":
    update_readme_date()
