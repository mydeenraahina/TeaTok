from run import app,get_products,clicked_product
import unittest

class Testing(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        self.client.testing=True

    def test_case_1(self):
        res=self.client.get('/')
        self.assertEqual(res.status_code,200)
        self.assertEqual(isinstance(get_products),dict)
   
    def test_case_2(self):
        res=self.client.get('/click')
        self.assertEqual(res.status_code,200)
        data=res.get_json()
        self.assertEqual(data,{"message":"Thanks For Ordering We will get back soonwith your order"})
if __name__=="__main__":
    unittest.main()
    