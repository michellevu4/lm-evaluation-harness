from promptsource import s

T0_EVAL = [
    ("super_glue", "wsc.fixed"),  # Coreference Resolution
    ("winogrande", "winogrande_xl"),  # Coreference Resolution
    ("super_glue", "cb"),  # Natural Language Inference
    ("super_glue", "rte"),  # Natural Language Inference
    ("anli", None),  # Natural Language Inference
    ("super_glue", "copa"),  # Sentence Completion
    ("hellaswag", None),  # Natural Language Inference
    ("super_glue", "wic"),  # Word Sense Disambiguation
]

for dataset_path, dataset_name in T0_EVAL:

    pass
    # "include: promptsource_template.yaml"
    # use_prompts:
