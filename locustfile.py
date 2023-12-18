from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def HomePage(self):
        self.client.get("/")