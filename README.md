# Django One-to-Many Example (ForeignKey)

This project is an example of Django's one-to-many relationships with `ForeignKey`.

This example uses Django Rest Framework (version `~= 3.14`).

## Requirements

This project was created on macOS version `14.2 Sonoma` with C Python version `3.11.6`. See [requirements.txt.lock](./requirements.txt.lock) for python packages and versions used in development.

The python packages listed in [requirements.txt](./requirements.txt) must be installed:

```shell
cd path/to/django-foreignkey-example
pip install --requirement requirements.txt
```

In `requirements.txt`:

```text
django              ~= 5.0
djangorestframework ~= 3.14
```

## Scripts (macOS)

See `scripts` for build scripts for common actions. Note that these scripts were written for `macOS`.

## Embedded Models

The example is of a car garage. Each garage can have many cars (one-to-many), and each car can have many wheels (one-to-many, hopefully 4 🙂).

The models are pretty straightforward. The `GarageSerializer` is more interesting.

It is worth noting that `ModelSerializer` and `HyperlinkModelSerializer` have a `Meta` class property called `depth`, which will return the embedded data up to the specified depth.

`depth` does not offer any control over the serialization for the embedded models. If you want to control of the fields and  serialization you have to subclass `Serializer` and populate it with the fields you want. These can be built-in serializer fields like `CharField`. Custom fields can be created; this project uses a custom `CarField`, for example, to be able to control which cars are returned: the custom method `CarField.get_queryset` only returns cars that belong to the current user.

We can also use other serializers in our serializer class. For example, `GarageSerializer` has a field which uses `CarSerializer(many=True)` to serialize the one-to-many `Garage.cars` field (renamed from `car_set`).
