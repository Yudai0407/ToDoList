import json
from datetime import datetime

DATA_FILE = 'tasks.json'

# タスクを読み込む関数
def load_tasks():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# タスクを保存する関数
def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

# タスクを追加する関数
def add_task():
    title = input("タスクのタイトルを入力してください: ")
    description = input("タスクの説明を入力してください: ")
    deadline = input("締め切り日を入力してください (YYYY-MM-DD): ")
    status = "未完了"  # 初期状態は「未完了」

    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'deadline': deadline,
        'status': status,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)

    print("タスクが追加されました！")
    print(json.dumps(new_task, ensure_ascii=False, indent=4))

# タスクをリスト表示する関数
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("タスクはまだありません。")
    else:
        print("タスク一覧:")
        for task in tasks:
            print(json.dumps(task, ensure_ascii=False, indent=4))

# メインメニュー
def main():
    while True:
        print("\nToDoリストアプリ")
        print("1. タスクを追加")
        print("2. タスク一覧を表示")
        print("3. 終了")

        choice = input("選択肢を入力してください (1/2/3): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("アプリケーションを終了します。")
            break
        else:
            print("無効な選択肢です。再度お試しください。")

if __name__ == "__main__":
    main()
