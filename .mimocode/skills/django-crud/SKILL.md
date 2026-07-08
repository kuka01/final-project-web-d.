---
name: django-crud
description: Add CRUD operations for a new model to this Django REST API project, including model, serializer, API views, URLs, admin, and migrations.
---

# Django REST API CRUD Skill

Add complete CRUD operations for a new model to this Django REST API project.

## Input

- **Model name** (e.g., "Transaction", "Payment", "Category")
- **Fields** (name, type, options)
- **Permissions** (optional: public read, authenticated write)

## Procedure

### Step 1: Read Existing Code Structure
Read these files to understand patterns:
- `store/models.py` - existing models
- `store/serializers.py` - serializer patterns
- `store/api_views.py` - API view patterns (FBV and CBV)
- `store/urls.py` - URL patterns
- `store/admin.py` - admin registration

### Step 2: Create/Update Model
Add model to `store/models.py`:
- Follow existing patterns (inherit from `models.Model`)
- Include `created_at`, `updated_at` fields
- Add `__str__` method
- Add `verbose_name` / `verbose_name_plural`

### Step 3: Create Serializer
Add serializer to `store/serializers.py`:
- Inherit from `serializers.ModelSerializer`
- Add `username` (read-only) if model has `user` field
- Add `status_display`, `payment_method_display` (read-only) if applicable
- Configure `Meta.fields` and `Meta.read_only_fields`

### Step 4: Create API Views
Add to `store/api_views.py`:

**List/Create (FBV):**
```python
@api_view(['GET', 'POST'])
def api_<model>_list(request):
    if request.method == 'GET':
        # List logic with filters
    elif request.method == 'POST':
        # Create logic with serializer validation
```

**Detail/Update/Delete (FBV or CBV):**
```python
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_<model>_detail(request, pk):
    # Get object or 404
    # Handle GET, PUT, PATCH, DELETE
```

**Imports to add:**
```python
from .models import <ModelName>
from .serializers import <ModelName>Serializer
```

### Step 5: Update URLs
Add to `store/urls.py`:
```python
path("api/<model>s/", api_views.api_<model>_list, name="api_<model>_list"),
path("api/<model>s/<int:pk>/", api_views.api_<model>_detail, name="api_<model>_detail"),
```

### Step 6: Update Admin
Add to `store/admin.py`:
```python
@admin.register(<ModelName>)
class <ModelName>Admin(admin.ModelAdmin):
    list_display = ['id', 'field1', 'field2', 'created_at']
    list_filter = ['status']
    search_fields = ['field1']
```

### Step 7: Run Migrations
```bash
python manage.py makemigrations store
python manage.py migrate
```

### Step 8: Test
```bash
python manage.py check
python manage.py check --deploy
```

## Stopping Condition

- All 5 files updated (models, serializers, api_views, urls, admin)
- Migrations applied successfully
- `python manage.py check` passes with no errors

## Example

User request: "Add CRUD for Transaction model with fields: amount, status, payment_method, description"

This skill will:
1. Add `Transaction` model to `store/models.py`
2. Add `TransactionSerializer` to `store/serializers.py`
3. Add `api_transaction_list` and `api_transaction_detail` to `store/api_views.py`
4. Add URL patterns to `store/urls.py`
5. Add `TransactionAdmin` to `store/admin.py`
6. Run migrations
7. Verify with `python manage.py check`
