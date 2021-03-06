from api.models import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    languages = db.Column(db.Text)
    development_status = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    release_date = db.Column(db.DateTime)
    users = db.relationship('UserHasProject', back_populates='project')
    links = db.relationship('ProjectLink', backref='project', lazy=True)

    def __repr__(self):
        return '<Project %r>' % self.name

class ProjectLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __repr__(self):
        return '<ProjectLink %r>' % self.name