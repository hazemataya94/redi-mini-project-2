list: ## Show available commands.
	@grep -E '^[a-zA-Z_-]+:.*?## ' Makefile | \
	awk -F ':.*?## ' '{printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | \
	sort

hello: ## prints hello world
	@echo "Hello, World!"

init: ## creates a virtual environment
	@[ ! -d ".venv" ] && python -m venv .venv || true
	@echo "$$ .venv/bin/python -m pip install -r requirements.txt"
	@.venv/bin/python -m pip install -r requirements.txt
	@echo "Virtual environment created and requirements installed"
	@echo "Run the following to start virtual env"
	@echo "\$$ source .venv/bin/activate"
	
freeze: ## freezes the requirements
	@.venv/bin/python -m pip freeze > requirements.txt
	@echo "Requirements frozen"

generate-ssh-key: ## generates a ssh key
	@ssh-keygen -t rsa -b 4096 -C "hazem-redi"