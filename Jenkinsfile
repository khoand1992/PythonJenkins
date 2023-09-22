pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('install virtualenv') {
      steps {
        sh 'pip install virtualenv'
      }
    }
    stage('init virtualenv') {
      steps {
        sh 'python3 -m virtualenv venv'
      }
    }
    stage('enable virtualenv') {
      steps {
        sh 'source venv/bin/activate'
      }
    }
    stage('install requirements.txt') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('run hello') {
      steps {
        sh 'python hello.py'
      }
    }
  }
  post {
    failure {
        mail bcc: '', body: "<b>Example</b><br>Project: Build Tool <br>, cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI, to: "kayd200123@gmail.com";
    }
  }
}