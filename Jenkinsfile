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
        emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
    }
  }
}