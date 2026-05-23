from sqlalchemy.orm import Session
from model.post import Post
from schemas.post import PostCreate, PostUpdate


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

def get_posts_controller(db: Session):
    return db.query(Post).order_by(Post.created_at.desc()).all()

def get_post_specific_controller(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post:
        post.view_count += 1
        db.commit()
        db.refresh(post)

    return post

def delete_post_controller(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    db.delete(post)
    db.commit()

    return post


def update_post_controller(db: Session, post_id: int, post_update: PostUpdate):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    update_data = post_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(post, key, value)

    db.commit()
    db.refresh(post)

    return post
