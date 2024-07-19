import unittest
from airflow.models import DagBag

class TestExampleDag(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag()

    def test_dag_loaded(self):
        dag_id = 'example_dag'
        dag = self.dagbag.get_dag(dag_id)
        self.assertDictEqual(self.dagbag.import_errors, {})
        self.assertIsNotNone(dag)
        self.assertEqual(dag_id, dag.dag_id)

    def test_dag_structure(self):
        dag = self.dagbag.get_dag('example_dag')
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['start', 'end'])

    def test_task_dependencies(self):
        dag = self.dagbag.get_dag('example_dag')
        start_task = dag.get_task('start')
        end_task = dag.get_task('end')
        self.assertIn(end_task, start_task.downstream_list)
        self.assertIn(start_task, end_task.upstream_list)

if __name__ == '__main__':
    unittest.main()
