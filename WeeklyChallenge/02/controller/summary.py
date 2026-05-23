import yaml
from ollama import chat
from sqlalchemy.orm import Session

from model.post import Post
from model.comment import Comment


def load_prompts():
    with open("prompts.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def call_ollama(model: str, system_prompt: str, user_prompt: str):
    response = chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.message.content

def summarize_post_with_comments_controller(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    comments = (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .order_by(Comment.created_at.asc())
        .all()
    )

    if comments:
        comments_text = "\n".join(
            [
                f"- {comment.author}: {comment.content}"
                for comment in comments
            ]
        )
    else:
        comments_text = "댓글 없음"

    prompts = load_prompts()
    prompt_data = prompts["summarize_post_with_comments"]

    user_prompt = prompt_data["user"].format(
        post_title=post.title,
        post_content=post.content,
        comments_text=comments_text
    )

    return call_ollama(
        model=prompt_data["model"],
        system_prompt=prompt_data["system"],
        user_prompt=user_prompt
    )
