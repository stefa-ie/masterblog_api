from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    sort_field = request.args.get('sort')
    direction = request.args.get('direction', 'asc').lower()

    # If no sort parameter, return posts in original order
    if not sort_field:
        return jsonify(POSTS), 200

    # Validate sort field
    if sort_field not in ('title', 'content'):
        return jsonify({"error": "Invalid sort field. Must be 'title' or 'content'."}), 400

    # Validate direction
    if direction not in ('asc', 'desc'):
        return jsonify({"error": "Invalid direction. Must be 'asc' or 'desc'."}), 400

    # Create a sorted copy to avoid modifying the original list
    sorted_posts = sorted(POSTS, key=lambda p: p[sort_field].lower(), reverse=(direction == 'desc'))
    return jsonify(sorted_posts), 200


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_search = request.args.get('title', '').strip()
    content_search = request.args.get('content', '').strip()

    results = []
    for post in POSTS:
        title_match = not title_search or title_search.lower() in post['title'].lower()
        content_match = not content_search or content_search.lower() in post['content'].lower()
        if title_match and content_match:
            results.append(post)

    return jsonify(results), 200


@app.route('/api/posts', methods=['POST'])
def add_post():
    blog_posts = request.get_json()

    if blog_posts is None:
        return jsonify({"error": "Invalid JSON format"}), 400

    if "title" not in blog_posts or "content" not in blog_posts:
        return jsonify({"error": "Missing title or content"}), 400

    new_post = {
        "id": len(POSTS) + 1,
        "title": blog_posts["title"],
        "content": blog_posts["content"]
    }

    POSTS.append(new_post)
    return jsonify(new_post), 201


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    for post_to_delete in POSTS:
        if post_to_delete["id"] == id:
            POSTS.remove(post_to_delete)
            return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200
    return jsonify({"error": f"Post with {id} does not exist."}), 404


@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    update_blog_post = request.get_json()

    if update_blog_post is None:
        return jsonify({"error": "Invalid JSON format"}), 400

    for post_to_update in POSTS:
        if post_to_update["id"] == id:
            if "title" in update_blog_post:
                post_to_update["title"] = update_blog_post["title"]
            if "content" in update_blog_post:
                post_to_update["content"] = update_blog_post["content"]
            return jsonify({"message": f"Post with id {id} has been updated successfully."}), 200
    return jsonify({"error": f"Post with {id} does not exist."}), 404




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
