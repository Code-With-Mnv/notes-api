from flask import blueprints, request, jsonify
from app import db
from app.models import Note

note_routes_bp = blueprints.Blueprint('note_routes', __name__)

@note_routes_bp.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()

    result = []

    for note in notes:
        result.append({
            'id': note.id,
            'title': note.title,
            'content': note.content
        })

    return jsonify(result)

@note_routes_bp.route('/add-note', methods=['POST'])
def create_note():
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    
    new_note = Note(title=title, content=content)
    db.session.add(new_note)
    db.session.commit()

    return jsonify({'message':"Note created successfully", 'id': new_note.id}), 201