from sqlalchemy.orm import Session
from model.post import Post
from model.comment import Comment
from schemas.comment import CommentCreate, CommentUpdate


def create_comment_controller(db: Session, post_id: int, comment: CommentCreate):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    new_comment = Comment(
        post_id=post_id,
        content=comment.content,
        author=comment.author
    )

    db.add(new_comment)
    post.comment_count += 1

    db.commit()
    db.refresh(new_comment)

    return new_comment

def get_comments_controller(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    return (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .order_by(Comment.created_at.desc())
        .all()
    )

def update_comment_controller(
    db: Session,
    post_id: int,
    comment_id: int,
    comment_update: CommentUpdate
):
    comment = (
        db.query(Comment)
        .filter(Comment.id == comment_id, Comment.post_id == post_id)
        .first()
    )

    if not comment:
        return None

    update_data = comment_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(comment, key, value)

    db.commit()
    db.refresh(comment)

    return comment

def delete_comment_controller(db: Session, post_id: int, comment_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    comment = (
        db.query(Comment)
        .filter(Comment.id == comment_id, Comment.post_id == post_id)
        .first()
    )

    if not comment:
        return None

    db.delete(comment)

    if post.comment_count > 0:
        post.comment_count -= 1

    db.commit()

    return comment
