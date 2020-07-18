package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICooling;
import www.google.com.digitalbuildings._0_0_1.subfields.IRequest;
import www.google.com.digitalbuildings._0_0_1.subfields.ICount;

public interface ICooling_request_count extends IField{

	public IRI iri();

    public void addComposedOfCooling (ICooling parameter);

	public Set<ICooling> getComposedOfCooling();

    public void addComposedOfCount (ICount parameter);

	public Set<ICount> getComposedOfCount();

    public void addComposedOfRequest (IRequest parameter);

	public Set<IRequest> getComposedOfRequest();

}