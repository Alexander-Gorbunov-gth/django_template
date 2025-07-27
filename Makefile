.PHONY: run
run:
	@docker compose build && docker compose up

.PHONY: res_main
res_main:
	@svo up -d --build django_partner

