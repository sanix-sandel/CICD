pipeline{
    agent {
        kubernetes {

          label 'k8s'

        }
    }

    stages{

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    kubernetesDeploy(
                        configFile: 'deployment.yaml',
//                         kubeconfigId: 'k8s'
                    )
                }
            }
        }
    }

}
