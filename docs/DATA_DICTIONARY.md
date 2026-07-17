# Data dictionary

## Master observation fields

- `source_id`: stable identifier for the source or source family.
- `source_title`: source title.
- `data_period_start`, `data_period_end`: dates when the evidence condition or activity occurred.
- `reference_year`: year used in yearly views.
- `geography`: place to which the value applies.
- `scope`: facility, programme, sample, or national denominator.
- `domain`: analytical category.
- `metric`: normalized data-point name.
- `value`: machine-readable numeric value when available.
- `value_text`: source wording or formatted value.
- `unit`: unit of measurement.
- `status`: actual, baseline, estimate, projection, target, budget, capacity, standard, derived, or context.
- `denominator`: explicit denominator where available.
- `facility_level`: reported facility type or level.
- `source_reference`: page, table, line, citation, or URL.
- `notes`: interpretation and comparability guidance.
- `quality_flag`: conflict, limitation, or evidence-strength marker.

## Blank values

A blank value means the source did not publish a usable comparable value. It does not mean zero.
