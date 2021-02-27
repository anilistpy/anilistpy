use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod studio;

#[pyfunction]
fn videoLink(site: String, id: String) -> PyResult<String> {    
    if site == "youtube" {
            Ok(format!("https://youtu.be/{}", id))    
        }
    else{
            Ok("error".to_string()) 
        }
    }

#[pyfunction]
fn __ver__() -> PyResult<String> {
    let ver = "0.1.0";
    Ok(ver.to_string())
}

#[pyfunction]
fn __studio_test() -> PyResult<String>{
    match studio::__studio_test0(){
        Ok(res) => {Ok(format!("{}",res))}
        Err(_err) => {Ok(format!("Error"))}
    }    
    //Ok(format!("{:?}", studio::__studio_test0()))
   }

#[pymodule]
fn anilistpy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(__ver__, m)?)?;
    m.add_function(wrap_pyfunction!(videoLink, m)?)?;
    m.add_function(wrap_pyfunction!(__studio_test, m)?)?;
    Ok(())
}
