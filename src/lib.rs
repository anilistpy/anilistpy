use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

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

#[pymodule]
fn anilistpy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(__ver__, m)?)?;
    m.add_function(wrap_pyfunction!(videoLink, m)?)?;
    Ok(())
}
