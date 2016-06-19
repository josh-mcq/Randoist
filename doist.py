import todoist, random
from .config import EMAIL, PASSWORD

class Randoist(object):
    def __init__(self, user, password):
        self.api = todoist.TodoistAPI()
        self.user = self.api.user
        self.user.login(user, password)
        self.user.sync()
        self.all_items = self.api.projects.state['items']
        

    def sync(self):
        self.api.sync()
        self.all_items = self.api.projects.state['items']

#todo: eliminate any things that are due tomorrow or later.
#todo: show more info, like due date string, project, and priority
#todo: add a flag that allows specification of a project
#todo: add a flag that 
#todo: add more configuration options in config file..  such as how to weight things, look at repetitions for ideas..
#   should items with due dates get precedence?
#todo: for each day late, it should add one more into the weighted list
#todo: come up with a more elegant way of weighting than merely a list. each item would have a priority and then the picker would keep picking until it reached the same one was picked twice within a queue length of like 5.
    def draw(self):
        l = self.create_weighted_list()
        task = random.choice(l)
        self.last_task = task
        self.remove_from_list(task)
        return task
        #list.remove(x) for x in filter(lambda x:x==self.last_task,list)
        #compile list of tasks, with different occurences based on weight
        #grab random task from self.all_items
        #set self.last_task to that task
        #delete task from all_items

    def create_weighted_list(self):
        result = []
        for item in self.all_items:
            for _ in range(item['priority']):
                result.append(item['content'])
        return result

    def remove_from_list(self, thing):
        for item in self.all_items:
            if item['content']==thing:
                self.all_items.remove(item)

todoist = Randoist(EMAIL, PASSWORD)
print ('todoist is ready, try typing todoist.draw()')
