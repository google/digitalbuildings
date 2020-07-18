package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IExhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.IFlowrate;
import www.google.com.digitalbuildings._0_0_1.subfields.ICapacity;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;

public interface IExhaust_air_flowrate_capacity extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfCapacity (ICapacity parameter);

	public Set<ICapacity> getComposedOfCapacity();

    public void addComposedOfExhaust (IExhaust parameter);

	public Set<IExhaust> getComposedOfExhaust();

    public void addComposedOfFlowrate (IFlowrate parameter);

	public Set<IFlowrate> getComposedOfFlowrate();

}