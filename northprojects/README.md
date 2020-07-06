# North Projects

## Development

### Django

Make a virtual environment (`virtualenv env`), and source it `source env/bin/activate`.

Then just run

```sh
python manage.py runserver
```

### Parcel (frontend assets)

Make sure all packages are installed by running `yarn`, then

```
yarn watch
```

## Conventions

### Git

Write clear and descriptive commit messages, in present tense, eg:

> Add hero block

or 

> Update styling for menu on mobile devices

## Required tooling

- black (for Python formatting)
- prettier (for Sass & Typescript formatting)
- yarn (for node packages, rather than npm)