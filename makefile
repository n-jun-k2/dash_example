requirements:
	@docker-compose run --rm pip-tools
	@docker rmi pyenv_pip-tools