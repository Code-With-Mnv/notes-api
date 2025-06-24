from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models import Note

note_routes_bp = Blueprint('note_routes', __name__)

@note_routes_bp.route('/notes', methods=['GET'])
def get_notes():
    try:
        notes = Note.query.all()
        result = [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]
        current_app.logger.info(f"Fetched {len(result)} notes.")
        return jsonify(result)
    except Exception as e:
        current_app.logger.error(f"Failed to fetch notes: {str(e)}", exc_info=True)
        return jsonify({'error': 'Failed to retrieve notes'}), 500

@note_routes_bp.route('/add-note', methods=['POST'])
def create_note():
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')

        if not title or not content:
            current_app.logger.warning("POST /add-note failed: Missing title or content.")
            return jsonify({'error': 'Title and content are required'}), 400
        
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()

        current_app.logger.info(f"Note created with ID {new_note.id}")
        return jsonify({'message': "Note created successfully", 'id': new_note.id}), 201

    except Exception as e:
        current_app.logger.error(f"Error while creating note: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal Server Error'}), 500

@note_routes_bp.route('/delete-note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        note = Note.query.get(note_id)

        if not note:
            current_app.logger.warning(f"DELETE /delete-note/{note_id} failed: Note not found.")
            return jsonify({'error': 'Note not found'}), 404
        
        db.session.delete(note)
        db.session.commit()

        current_app.logger.info(f"Deleted note with ID {note_id}")
        return jsonify({'message': 'Note deleted successfully'}), 200

    except Exception as e:
        current_app.logger.error(f"Error deleting note ID {note_id}: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal Server Error'}), 500