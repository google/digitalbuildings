package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
/**
* Class Field 
* The class of all fields
*/
public interface IField extends IRI{

	public IRI iri();


	public void setTimeSeriesId (String parameter);

	public String getTimeSeriesId ();
}