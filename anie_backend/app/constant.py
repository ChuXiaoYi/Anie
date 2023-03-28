from enum import Enum


class Gender(Enum):
    MAN = 1
    WOMAN = 2


class AnimalCategoryEnum(Enum):
    DOG = 1
    CAT = 2


class DogSubCategoryEnum(Enum):
    PUG = 1
    LABRADOR = 2
    BULLDOG = 3


class CatSubCategoryEnum(Enum):
    PERSIAN = 1
    SIAMESE = 2
    BENGAL = 3


ANIMAL_MAP = {
    AnimalCategoryEnum.DOG: DogSubCategoryEnum,
    AnimalCategoryEnum.CAT: CatSubCategoryEnum
}
