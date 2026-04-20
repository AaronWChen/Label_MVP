from .warning_validator import validate_warning


def verify(fields, raw_text):
    warning = validate_warning(raw_text)

    return {
        "warning": warning,
        "overall_pass": warning["is_valid"]
    }
