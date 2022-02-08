# TO_DO list on Django/with with authentication and registration

This project was created as the MidTerm assignment for the Advanced Programming 2 course. 
It is a website with login and registration forms. There is also, list of tasks. You can add new task, update and delete existing task, and searching function.
Connected database: PostgreSQL

### Installation
Copy from source
```bash
git clone https://github.com/Assylken/DjangoAss1.git
```

### Usage

```
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
```

### Examples
Login page: <br />
<img src="/images/login.png" width="600" height="300"/> <br />
Register page: <br />
<img src="/images/register.png" width="600" height="300"/> <br />
Task list page with search, add, update, delete methods: <br />
<img src="/images/task_list.png" width="600" height="300"/>
