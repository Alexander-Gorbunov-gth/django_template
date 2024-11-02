.PHONY: run
run:
	@python3 manage.py runserver

.PHONY: docker
docker:
	@docker buildx build --platform=linux/amd64 -t csdochub/django_partner . &&  docker push csdochub/django_partner