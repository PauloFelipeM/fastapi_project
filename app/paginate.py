from fastapi import Request


def paginate(model, request: Request):
    params = dict(request.query_params)
    page = 1
    per_page = 5

    if 'page' in params and params['page'].isnumeric():
        page = int(params['page'])

    if 'per_page' in params and params['per_page'].isnumeric():
        per_page = int(params['per_page'])

    total = model.query.count()
    last_page = (total // per_page)

    page_obj = model.query.offset((page - 1) * per_page).limit(per_page).all()

    if page >= last_page:
        next = None
    else:
        next = page + 1

    if page <= 1:
        prev = None
    else:
        prev = page - 1

    if last_page <= 0:
        last_page = 1

    return {
        'results': page_obj,
        'page': page,
        'per_page': per_page,
        'next': next,
        'prev': prev,
        'total': total,
        'last_page': last_page,
    }
