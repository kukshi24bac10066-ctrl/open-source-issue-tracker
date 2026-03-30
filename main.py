import json
import os

FILE = "issues.json"

def load_issues():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_issues(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_issue():
    title = input("Enter issue title: ")
    description = input("Enter issue description: ")

    issues = load_issues()
    issue_id = len(issues) + 1

    issues.append({
        "id": issue_id,
        "title": title,
        "description": description,
        "status": "open"
    })

    save_issues(issues)
    print("✅ Issue added successfully!")

def view_issues():
    issues = load_issues()

    if not issues:
        print("No issues found.")
        return

    print("\n📋 All Issues:")
    for issue in issues:
        print(f"[{issue['id']}] {issue['title']} - {issue['status']}")

def close_issue():
    issues = load_issues()

    if not issues:
        print("No issues to close.")
        return

    issue_id = int(input("Enter issue ID to close: "))

    for issue in issues:
        if issue["id"] == issue_id:
            issue["status"] = "closed"
            save_issues(issues)
            print("✅ Issue closed!")
            return

    print("❌ Issue not found.")

def search_issue():
    keyword = input("Enter keyword to search: ")
    issues = load_issues()

    found = False
    for issue in issues:
        if keyword.lower() in issue["title"].lower():
            print(f"[{issue['id']}] {issue['title']} - {issue['status']}")
            found = True

    if not found:
        print("No matching issues found.")

def menu():
    while True:
        print("\n===== Issue Tracker =====")
        print("1. Add Issue")
        print("2. View Issues")
        print("3. Close Issue")
        print("4. Search Issue")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_issue()
        elif choice == "2":
            view_issues()
        elif choice == "3":
            close_issue()
        elif choice == "4":
            search_issue()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()