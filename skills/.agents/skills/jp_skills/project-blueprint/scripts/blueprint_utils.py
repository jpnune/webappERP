import os
import datetime
import sys

def init_project():
    """Initializes the planning document structure in the /docs directory."""
    docs_dir = "docs"
    files = ["PRD.md", "Roadmap.md", "Analytics_Architecture.md", "Risk_Analysis.md", "implementation_log.md"]
    
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)
        print(f"Created directory: {docs_dir}")

    for file in files:
        file_path = os.path.join(docs_dir, file)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {file.replace('.md', '').replace('_', ' ')}\n")
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")

def log_entry(message, action_id="GENERAL"):
    """Adds an entry to the immutable implementation log (append-only)."""
    log_path = os.path.join("docs", "implementation_log.md")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n---\n## [{timestamp}] - {action_id}\n- {message}\n"
    
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)
    print("Log entry added (Append-only).")

if __name__ == "__main__":
    if "--init" in sys.argv:
        init_project()
    elif "--log" in sys.argv:
        msg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "No message provided"
        log_entry(msg)
