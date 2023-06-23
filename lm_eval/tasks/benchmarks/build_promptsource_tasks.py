from promptsource.templates import DatasetTemplates

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

for dataset_name, subset_name in T0_EVAL:

    if subset_name is None:
        prompts = DatasetTemplates(dataset_name=dataset_name)
    else:
        prompts = DatasetTemplates(dataset_name=dataset_name, subset_name=subset_name)

    for prompt_name in prompts.all_template_names:
        config_dict = {
            "include: promptsource_template.yaml" "use_prompts": prompts[prompt_name]
        }
