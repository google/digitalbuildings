package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IHeating;
import www.google.com.digitalbuildings._0_0_1.subfields.IRequest;
import www.google.com.digitalbuildings._0_0_1.subfields.ICount;

public interface IHeating_request_count extends IField{

	public IRI iri();

    public void addComposedOfCount (ICount parameter);

	public Set<ICount> getComposedOfCount();

    public void addComposedOfHeating (IHeating parameter);

	public Set<IHeating> getComposedOfHeating();

    public void addComposedOfRequest (IRequest parameter);

	public Set<IRequest> getComposedOfRequest();

}