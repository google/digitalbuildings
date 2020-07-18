package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IRequest;
import www.google.com.digitalbuildings._0_0_1.subfields.ICount;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressurization;

public interface IPressurization_request_count extends IField{

	public IRI iri();

    public void addComposedOfCount (ICount parameter);

	public Set<ICount> getComposedOfCount();

    public void addComposedOfPressurization (IPressurization parameter);

	public Set<IPressurization> getComposedOfPressurization();

    public void addComposedOfRequest (IRequest parameter);

	public Set<IRequest> getComposedOfRequest();

}