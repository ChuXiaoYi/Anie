import json

from PIL import Image

from app.utils.upload2ipfs import pin_file, pin_json

FIRST_NAMES = ['Herbie', 'Sprinkles', 'Boris', 'Dave', 'Randy', 'Captain']
LAST_NAMES = ['Starbelly', 'Fisherton', 'McCoy']

BASES = ['jellyfish', 'starfish', 'crab', 'narwhal', 'tealfish', 'goldfish']
EYES = ['big', 'joy', 'wink', 'sleepy', 'content']
MOUTH = ['happy', 'surprised', 'pleased', 'cute']

INT_ATTRIBUTES = [5, 2, 3, 4, 8]
FLOAT_ATTRIBUTES = [1.4, 2.3, 11.7, 90.2, 1.2]
STR_ATTRIBUTES = [
    'happy',
    'sad',
    'sleepy',
    'boring'
]
BOOST_ATTRIBUTES = [10, 40, 30]
PERCENT_BOOST_ATTRIBUTES = [5, 10, 15]
NUMBER_ATTRIBUTES = [1, 2, 1, 1]


def creature(token_id):
    token_id = int(token_id)
    num_first_names = len(FIRST_NAMES)
    num_last_names = len(LAST_NAMES)
    creature_name = "%s %s" % (FIRST_NAMES[token_id % num_first_names], LAST_NAMES[token_id % num_last_names])

    base = BASES[token_id % len(BASES)]
    eyes = EYES[token_id % len(EYES)]
    mouth = MOUTH[token_id % len(MOUTH)]
    image_path = _compose_image(['/Users/chuxiaoyi/work/AnieWorld/anie_backend/app/utils/images/bases/base-%s.png' % base,
                                 '/Users/chuxiaoyi/work/AnieWorld/anie_backend/app/utils/images/eyes/eyes-%s.png' % eyes,
                                 '/Users/chuxiaoyi/work/AnieWorld/anie_backend/app/utils/images/mouths/mouth-%s.png' % mouth],
                                token_id)

    attributes = []
    _add_attribute(attributes, 'base', BASES, token_id)
    _add_attribute(attributes, 'eyes', EYES, token_id)
    _add_attribute(attributes, 'mouth', MOUTH, token_id)
    _add_attribute(attributes, 'level', INT_ATTRIBUTES, token_id)
    _add_attribute(attributes, 'stamina', FLOAT_ATTRIBUTES, token_id)
    _add_attribute(attributes, 'personality', STR_ATTRIBUTES, token_id)
    _add_attribute(attributes, 'aqua_power', BOOST_ATTRIBUTES, token_id, display_type="boost_number")
    _add_attribute(attributes, 'stamina_increase', PERCENT_BOOST_ATTRIBUTES, token_id, display_type="boost_percentage")
    _add_attribute(attributes, 'generation', NUMBER_ATTRIBUTES, token_id, display_type="number")

    image_url = pin_file(image_path)

    return pin_json({
        'name': creature_name,
        'description': "Friendly OpenSea Creature that enjoys long swims in the ocean.",
        'image': image_url,
        'external_url': 'https://example.com/?token_id=%s' % token_id,
        'attributes': attributes
    })


def _add_attribute(existing, attribute_name, options, token_id, display_type=None):
    trait = {
        'trait_type': attribute_name,
        'value': options[token_id % len(options)]
    }
    if display_type:
        trait['display_type'] = display_type
    existing.append(trait)


def _compose_image(image_files, token_id, path="creature"):
    composite = None
    for image_file in image_files:
        foreground = Image.open(image_file).convert("RGBA")

        if composite:
            composite = Image.alpha_composite(composite, foreground)
        else:
            composite = foreground

    output_path = "/Users/chuxiaoyi/work/AnieWorld/anie_backend/app/utils/images/output/%s.png" % token_id
    composite.save(output_path)
    return output_path


if __name__ == '__main__':
    print(creature(3))
