import random
from locust import HttpUser, task, between


class MeuTeste(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(0.1, 0.5)

    @task
    def send_message(self):
        content = random.choice([
            "manda o relatório pra mim",
            "preciso falar com você",
            "me envia o arquivo excel",

            "você é muito burro",
            "faz isso direito anta",
            "que trabalho lixo",

            "manda foto sua 😏",
            "você tá muito gostosa hoje",
            "vamos fazer algo hoje 😉",
        ])

        self.client.post(
            f"/dummy/send?message={content}",
        )