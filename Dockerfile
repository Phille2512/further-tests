FROM python:3.10-alpine AS base 

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN PIP_USER=1 pip install pipenv
COPY Pipfile* ./
RUN PIP_USER=1 pipenv install --system --deploy

FROM python:3.10-alpine

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
COPY --chown=user:myapp --from=base ${PYROOT}/ ${PYROOT}/

RUN pip install uvicorn
RUN mkdir -p /usr/src/app
WORKDIR /usr/src

COPY --chown=user:myapp app ./app
USER 1234

CMD ["uvicorn", "app.main2:app", "--host", "0.0.0.0", "--port", "8080"]