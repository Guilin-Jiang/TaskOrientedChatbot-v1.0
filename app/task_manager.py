
import re

class TaskManager:
    def __init__(self):
        self.tasks = []

    def build(self, message: str):
        task = re.sub(r".*(创建|build|添加|新增)(一个)?", "", message, flags=re.IGNORECASE).strip()
        if task:
            self.tasks.append(task)

    def delete(self, message: str):
        task = re.sub(r".*(删除|删减|delete)(一个)?", "", message, flags=re.IGNORECASE).strip()
        if task in self.tasks:
            self.tasks.remove(task)

    def update(self, message: str):
        task = re.sub(r".*(完成|更新|finish|update)(一个)?", "", message, flags=re.IGNORECASE).strip()
        for i, t in enumerate(self.tasks):
            if task in t:
                self.tasks[i] = f"✅ {t.strip('✅ ').strip()}"
                break

    def get_all(self):
        return self.tasks
