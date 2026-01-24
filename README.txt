This is a simple terminal application that will implement my version of the bullet list.

Bullet lists are my way of organising my week, essentially a queue structure of all my upcoming tasks.
This works better than a timetable because it only focuses on what to do next, not when to do it.
The app is very simple, each task is appended to the end of the queue by default, with each task having three attributes:
   - description: what the task is.
   - due date: when the task has to be completed by
   - tag: a classification system to group tasks together e.g coursework or job applications.
Tasks can be reordered and also viewed in order from most to least urgent.
In this way overdue tasks are flagged and displayed on the top.

 LIST OF COMMANDS:

list - display the full list of tasks
   flags (optional):
      date - display the full list of tasks soonest first
      tag - display the full list of tasks by tag


new - add a new task
   after typing "new" the rest must follow in this exact format:

   DESCRIPTION|DATE/MONTH/YEAR|TAG

   **note: the DATE is in days, MONTH is out of 12, YEAR is strictly 4 digit**


complete - complete tasks and remove them from the list:
   after typing "complete" type the index of the tasks you want to complete
   all separated by a space

   EXAMPLE:
      complete 1 4
   this will remove items 1 and 4 from the list

save - save the list of tasks to the current active file

expand - expand on certain lists items by index:
   after typing "expand" type the index of the tasks you want to expand
   all separated by a space

help - display this full list of COMMANDS



TODO:
   make the date parse on entry