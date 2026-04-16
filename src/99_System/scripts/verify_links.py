import os
import re
import sys

def verify_links(base_dir):
    broken_links = []
    total_files = 0
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find markdown links: [text](path)
                links = re.findall(r'\[.*?\]\((?!http|mailto|#)(.*?)\)', content)
                
                for link in links:
                    # Clean up anchors
                    link_path = link.split('#')[0]
                    if not link_path:
                        continue
                        
                    # Target path relative to the current file's directory
                    target_abs_path = os.path.abspath(os.path.join(root, link_path))
                    
                    if not os.path.exists(target_abs_path):
                        broken_links.append((file_path, link))
                        
    return total_files, broken_links

if __name__ == "__main__":
    search_dir = sys.argv[1] if len(sys.argv) > 1 else 'src'
    print(f"Verifying links in: {search_dir}...")
    total, broken = verify_links(search_dir)
    
    print(f"Total files scanned: {total}")
    if broken:
        print(f"Found {len(broken)} broken links:")
        for file, link in broken:
            print(f"- In {file}: {link}")
        sys.exit(1)
    else:
        print("Success: No broken links found!")
        sys.exit(0)
