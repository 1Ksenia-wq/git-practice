# Отчёт по заданию (Git)

Проект: `git-practice`
Удалённый репозиторий: https://github.com/1Ksenia-wq/git-practice.git

## 1. Создание папки и инициализация

```bash
mkdir git-practice
cd git-practice
git init
```

## 2. Настройка user.name и user.email

```bash
git config --global user.name "Kseniia Boldyreva"
git config --global user.email "kseniaboldyreva1999@gmail.com"
```

(Настройки уже были заданы глобально; локальная конфигурация не потребовалась.)

## 3. Три осмысленных коммита

| Коммит | Сообщение | Содержание |
| --- | --- | --- |
| `6a113a4` | Add project README with goals | Создан README.md с описанием проекта |
| `2ca94d3` | Add main.py with greet function | Добавлена функция приветствия `greet()` |
| `acfe4ef` | Add CLI arguments and usage docs | Добавлены аргументы командной строки и примеры использования |

## 4. Просмотр истории и изменений

```bash
git log
git log --oneline
git diff 6a113a4 2ca94d3 -- main.py
git diff 2ca94d3 acfe4ef -- README.md
```

История (кратко):

```
4964fc7 Merge pull request #1 from 1Ksenia-wq/hotfix
0e2a1fc Resolve README conflict between main and hotfix
654e47b Update README goal in main
c489293 Update README goal in hotfix
1125207 Merge feature branch
6ec410b Add farewell function and CLI flag
acfe4ef Add CLI arguments and usage docs
2ca94d3 Add main.py with greet function
6a113a4 Add project README with goals
```

## 5. GitHub: remote и push

```bash
gh repo create git-practice --public --source=. --remote=origin --push
# либо вручную:
git remote add origin https://github.com/1Ksenia-wq/git-practice.git
git push -u origin main
```

## 6. Клонирование и проверка истории

```bash
git clone https://github.com/1Ksenia-wq/git-practice.git git-practice-clone
cd git-practice-clone
git log --oneline
git status --short --branch
```

Результат: `git log --oneline` в клоне показывает те же 9 коммитов, что и в
исходном репозитории; `git status` сообщает `## main...origin/main` без
изменений. История сохранена полностью.
