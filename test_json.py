#!/usr/bin/env python3
import json
import re

def extract_and_validate_json_specs(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all JSON script blocks
    pattern = r'<script type="application/json" id="([^"]+)">\s*(\{.*?\})\s*</script>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    results = {}
    for spec_id, json_content in matches:
        try:
            parsed = json.loads(json_content.strip())
            results[spec_id] = {'status': '✅ Valid', 'schema': parsed.get('$schema', 'Not found')}
        except json.JSONDecodeError as e:
            results[spec_id] = {'status': f'❌ Invalid: {e}', 'error_pos': e.pos if hasattr(e, 'pos') else 'Unknown'}
    
    return results

# Test the current index.html
results = extract_and_validate_json_specs('index.html')
print("JSON Specification Validation Results:")
print("=" * 50)
for spec_id, info in results.items():
    print(f"{spec_id}: {info['status']}")
    if 'schema' in info:
        print(f"  Schema: {info['schema']}")
    if 'error_pos' in info:
        print(f"  Error Position: {info['error_pos']}")
    print()