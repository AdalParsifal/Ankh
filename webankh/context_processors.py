def ankh_context(request):
    return {
        'es_mason': request.session.get('es_mason', False),
        'idioma': request.session.get('idioma', 'es'),
    }