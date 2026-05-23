from sqlalchemy.orm import Session
from model.post import Post
from schemas.post import PostCreate


def create_post_controller(db: Session, post: PostCreate):
    new_post = Post(
        title=post.title,
        content=post.content,
        author=post.author
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
