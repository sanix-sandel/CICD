pipeline{
    agent {
        kubernetes {

          label 'k8s'

        }
    }

    stages{

        stage('Deploy to Kubernetes') {
            kubernetesDeploy(
              configs: 'deployment.yaml',

              kubeconfigId: 'k8s'

            )
        }
    }

}
