use ureq;

/*
 * Test function: __studio_test()
 */
pub fn __studio_test0() -> String{
    let rt: String;    
    match __studio_test1(){
        Ok(response) => { rt = format!("{}", response); },
        Err(er) => { rt =  er.to_string(); }
    }
    
    return rt;
}

fn __studio_test1() -> Result<String, ureq::Error> {
    let body: String = ureq::post("https://graphql.anilist.co")
        .send_json(ureq::json!({
          "query": "query($id: Int){Studio(id: $id){name}}",
          "variables": {"id" : 1}
        }))?
        .into_string()?;
    
    Ok(body)
}
